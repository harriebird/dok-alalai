from datetime import date

def compute_age(birthday):
    today = date.today()
    age = today.year - birthday.year - ((today.month, today.day) < (birthday.month, birthday.day))
    return age

def compute_bmi(height, weight):
    height_meter = height / 100
    bmi = weight / (height_meter ** 2)
    return bmi

def format_assessment(assessment):
    assessment_info = ""
    for_female = ""

    personal_info = \
        f"""
Personal Information:
    Name: {assessment.client.first_name}{" " + assessment.client.middle_name + " " if assessment.client.middle_name else " "}{assessment.client.last_name}{" " + assessment.client.ext_name if assessment.client.ext_name else ""}
    Sex: {assessment.client.sex}
    Age: {compute_age(assessment.client.birth_date)}

    """
    assessment_info += personal_info

    if assessment.client.sex == "Female":
        for_female = \
            f"""

    Last menstrual period: {assessment.question7a}
    First menstrual period: {assessment.question7b}
    Number of pregnancy: {assessment.question7c}

    """

    assessment_response = \
        f"""
Review of Systems:
    Q: Chief complaint (please describe)
    A: {assessment.question1}

    Q: Do you experience any of the following: loss of appetite, lack of sleep, unexplained weight loss, feeling down/depressed, fever, headache, memory loss, blurring of vision, or hearing loss?
    A: {assessment.question2 if assessment.question2 else "No"}

    Q: Do you experience any of the following: cough/colds, chest pain, palpitations, or difficulty in breathing?
    A: {assessment.question3 if assessment.question3 else "No"}

    Q: Do you experience any of the following: abdominal pain, vomiting, change in bowel movement, rectal bleeding, or bloody/tarry stools?
    A: {assessment.question4 if assessment.question4 else "No"}

    Q: Do you experience any of the following: frequent urination, frequent eating, frequent intake of fluids?
    A: {assessment.question5 if assessment.question5 else "No"}

    Q: For male and female, do you experience ay of the following: pain or discomfort on urination, frequency of urination, dribbling of urine, pain during/after sex, blood in the urine, or foul-smelling genital discharge?
    A: {assessment.question6 if assessment.question6 else "No"}

    Q: Do you experience any of the following; muscle spasm, tremors, weakness; muscle/joint pain, stiffness, limitation of movement?
    A: {assessment.question8 if assessment.question8 else "No"}

    Q:
    A: {assessment.question4 if assessment.question4 else "No"}

    {for_female if assessment.client.sex == "Female" else ""}

    Personal/Social History:
    Q: Do you smoke cigar, cigarette, e-cigarette, vape, or other similar products?
    A: {f"Yes, for {assessment.smoke_years} years" if assessment.smoke_years else "No"}

    Q: Do you drink alcohol or alcohol-containing beverages?
    A: {f"Yes, for {assessment.alcohol_years} years" if assessment.alcohol_years else "No"}


    """
    assessment_info += assessment_response

    if assessment.medical_history:
        history_response = "Medical History:\n"

        for condition in assessment.medical_history:
            history_response += f"{condition.name}\n"

        assessment_info += history_response

    if assessment.physical_exam:
        physex = assessment.physical_exam
        physex_response = "Pertinent Physical Exam:\n"

        if physex.bp_systolic and physex.bp_diastolic:
            physex_response += f"Blood pressure: {physex.bp_systolic}/{physex.bp_diastolic} mmHg\n"

        if physex.blood_type:
            physex_response += f"Blood type: {physex.blood_type}\n"

        if physex.heart_rate:
            physex_response += f"Heart rate: {physex.heart_rate} bpm\n"

        if physex.respiration_rate:
            physex_response += f"Respiration rate: {physex.respiration_rate} breaths/min\n"

        if physex.va_top and physex.va_bottom:
            physex_response += f"Visual acuity: {physex.va_top}/{physex.va_bottom}\n"

        if physex.height:
            physex_response += f"Height: {physex.height} cm\n"

        if physex.weight:
            physex_response += f"Weight: {physex.weight} kg\n"

        if physex.height and physex.weight:
            physex_response += f"Body mass index: {compute_bmi(physex.height, physex.weight)} kg/m2\n"

        if physex.temperature:
            physex_response += f"Weight: {physex.temperature} °C\n"

        if physex.gen_survey:
            physex_response += f"Weight: {physex.gen_survey}\n"

        if physex.additional_notes:
            physex_response += f"Additional notes: {physex.additional_notes}\n"

        assessment_info += f"\n\n{physex_response}\n\n"

    if assessment.toddler_exam:
        toddler = assessment.toddler_exam
        toddler_exam_response = "Toddler Exam:\n"

        if toddler.length:
            toddler_exam_response += f"Length: {toddler.length} cm\n"

        if toddler.body_waist_circ:
            toddler_exam_response += f"Body waist circumference: {toddler.body_waist_circ} cm\n"

        if toddler.mid_upper_arm_circ:
            toddler_exam_response += f"Middle upper arm circumference: {toddler.mid_upper_arm_circ} cm\n"

        if toddler.head_circ:
            toddler_exam_response += f"Head circumference: {toddler.head_circ} cm\n"

        if toddler.hip:
            toddler_exam_response += f"Hip: {toddler.hip} cm\n"

        if toddler.skinfold_thick:
            toddler_exam_response += f"Skinfold thickness: {toddler.skinfold_thick} cm\n"

        if toddler.limbs:
            toddler_exam_response += f"Limbs: {toddler.limbs} cm\n"

        assessment_info += toddler_exam_response

    return assessment_info
