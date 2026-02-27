from ollama import Client
from sqlmodel import Session, select


from app.core import config
from app.core.assessment import format_assessment
from app.core.image import image_to_base64
from app.models import engine, Assessment, AssessmentFeedback

_llm_client = Client(host=config.OLLAMA_HOST)


async def analyze_image(image):

    base64_image = await image_to_base64(image)

    response = _llm_client.generate(
        model=config.OLLAMA_MODEL,
        prompt="Analyze this medical image and tell your findings. Be direct.",
        system="You're an expert doctor. You are good at analyzing medical images.",
        images=[base64_image]
    )

    return response.response


def analyze_assessment(assessment_uuid):
    assessment_info = ""
    with Session(engine) as session:
        assessment = session.exec(select(Assessment).where(Assessment.uuid == assessment_uuid)).first()
        if assessment:
            assessment_info = format_assessment(assessment)


        response = _llm_client.generate(
            model=config.OLLAMA_MODEL,
            prompt=f"Analyze the assessment form response and tell your findings. Recommended test to conduct if possible. Here's the response:\n\n {assessment_info}",
            system="You're an expert doctor. You are good at analyzing assessment forms. Give direct response instead making it conversational."
        )

        print(f"[DEBUG] response: {response.response}")

        clean_response = response.response.split("<unused95>")[1] if "<unused95>" in response.response else response.response

        feedback = AssessmentFeedback()
        feedback.assessment_id = assessment.id
        feedback.ai_feedback = clean_response
        session.add(feedback)
        session.commit()

