(function() {
    const md = window.markdownit()

    axios.get(`/api/ai-feedback/${feedback_uuid}`)
        .then((response) => {
            document.querySelector("#personal-info").disabled = true
            let feedbackInfo = response.data
            let analysisResult = md.render(feedbackInfo.ai_feedback)

            document.querySelector("#first_name").value = feedbackInfo.assessment.client.first_name
            document.querySelector("#middle_name").value = feedbackInfo.assessment.client.middle_name
            document.querySelector("#last_name").value = feedbackInfo.assessment.client.last_name
            document.querySelector("#ext_name").value = feedbackInfo.assessment.client.ext_name

            document.querySelector("#ai-feedback").innerHTML = analysisResult

            document.querySelector("#feedback_comment").value = feedbackInfo.feedback_comment
            document.querySelector("#feedback_rating").value = feedbackInfo.feedback_rating
        })

        document.querySelector("#form-submit-btn").onclick = (e) => {
            let comment = {}
            comment["feedback_comment"] = document.querySelector("#feedback_comment").value
            comment["feedback_rating"] = document.querySelector("#feedback_rating").value
            axios.patch(`/api/ai-feedback/${feedback_uuid}/comment`,
                comment
            )
        }

})();