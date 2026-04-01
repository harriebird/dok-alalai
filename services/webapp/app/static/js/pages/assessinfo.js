(function() {

    let toddler;

    axios.get(`/api/assessments/${assessment_uuid}`)
        .then((response) => {
            let assessInfo = response.data
            toddler = getAgeMonths(assessInfo.client.birth_date) <= 24

            document.querySelector("#personal-info").disabled = true
            document.querySelector("#systems-review-fs").disabled = true
            document.querySelector("#social-history-fs").disabled = true
            document.querySelector("#medical-history-fs").disabled = true
            document.querySelector("#physical-exam-fs").disabled = true
            document.querySelector("#for-toddler-fs").disabled = true

            document.querySelector("#first_name").value = assessInfo.client.first_name
            document.querySelector("#middle_name").value = assessInfo.client.middle_name
            document.querySelector("#last_name").value = assessInfo.client.last_name
            document.querySelector("#ext_name").value = assessInfo.client.ext_name
            document.querySelector("#birth_date").value = assessInfo.client.birth_date
            document.querySelector("#sex").value = assessInfo.client.sex
            document.querySelector("#civil_status").value = assessInfo.client.civil_status
            document.querySelector("#email").value = assessInfo.client.email
            document.querySelector("#contact_number").value = assessInfo.client.contact_number
            document.querySelector("#philhealth_number").value = assessInfo.client.philhealth_number

            if(assessInfo.client.sex === "Male") {
                document.querySelector("#female-only").classList.add("d-none")
            }
            else {
                document.querySelector("#question7a").value = assessInfo.question7a
                document.querySelector("#question7b").value = assessInfo.question7b
                document.querySelector("#question7c").value = assessInfo.question7c
            }

            document.querySelector("#question1").value = assessInfo.question1
            let yesNoQuestions = [2, 3, 4, 5, 6, 8]

            yesNoQuestions.forEach((number) => {
                if(assessInfo[`question${number}`]) {
                    document.querySelector(`#question${number}`).value = assessInfo[`question${number}`]
                    document.querySelector(`#q${number}-yes`).checked = true
                    document.querySelector(`#question${number}`).classList.remove("d-none")
                }
                else {
                    document.querySelector(`#q${number}-no`).checked = true
                }
            })

            if(assessInfo.smoke_years) {
                document.querySelector(`#question9`).value = assessInfo.smoke_years
                document.querySelector(`#q9-yes`).checked = true
                document.querySelector(`#question9`).classList.remove("d-none")
            }
            else {
                document.querySelector(`#q9-no`).checked = true
            }

            if(assessInfo.alcohol_years) {
                document.querySelector(`#question10`).value = assessInfo.smoke_years
                document.querySelector(`#q10-yes`).checked = true
                document.querySelector(`#question10`).classList.remove("d-none")
            }
            else {
                document.querySelector(`#q10-no`).checked = true
            }

            if(assessInfo.medical_history) {
                const input = document.querySelector("#med-hist-input");
                const container = document.querySelector("#med-hist-container");

                assessInfo.medical_history.forEach((condition) => {
                    addConditionBadge(condition.name, container, input)
                })
            }

            document.querySelector("#bp_systolic").value = assessInfo.physical_exam.bp_systolic
            document.querySelector("#bp_diastolic").value = assessInfo.physical_exam.bp_diastolic
            document.querySelector("#blood_type").value = assessInfo.physical_exam.blood_type
            document.querySelector("#heart_rate").value = assessInfo.physical_exam.heart_rate
            document.querySelector("#respiration_rate").value = assessInfo.physical_exam.respiration_rate
            document.querySelector("#va_top").value = assessInfo.physical_exam.va_top
            document.querySelector("#va_bottom").value = assessInfo.physical_exam.va_bottom
            document.querySelector("#height").value = assessInfo.physical_exam.height
            document.querySelector("#weight").value = assessInfo.physical_exam.weight
            document.querySelector("#temperature").value = assessInfo.physical_exam.temperature
            document.querySelector("#gen_survey").value = assessInfo.physical_exam.gen_survey
            document.querySelector("#additional_notes").value = assessInfo.physical_exam.additional_notes

            if(toddler) {
                document.querySelector("#length").value = assessInfo.toddler_exam.length
                document.querySelector("#body_waist_circ").value = assessInfo.toddler_exam.body_waist_circ
                document.querySelector("#mid_upper_arm_circ").value = assessInfo.toddler_exam.mid_upper_arm_circ
                document.querySelector("#head_circ").value = assessInfo.toddler_exam.head_circ
                document.querySelector("#hip").value = assessInfo.toddler_exam.hip
                document.querySelector("#skinfold_thick").value = assessInfo.toddler_exam.skinfold_thick
                document.querySelector("#limbs").value = assessInfo.toddler_exam.limbs
            }

            assessInfo.feedback.forEach((feedback) => {
                document.querySelector("#feedback-list")
                    .insertAdjacentHTML("beforeend",`
                        <a href="/ai-feedback/${ feedback.uuid }" class="list-group-item list-group-item-action py-3 lh-tight">
                            <div class="d-flex w-100 align-items-center justify-content-between">
                                <strong class="mb-1">AI Feedback #${ feedback.id }</strong>
                                <div class="mb-1 small"><i class="bi bi-star-fill"></i> Rating: ${ feedback.feedback_rating ? feedback.feedback_rating : "Not yet" }</div>
                            </div>
                            <div class="d-flex w-100 align-items-start align-items-md-center justify-content-between flex-column flex-md-row">
                                <div class="mb-1 small"><i class="bi bi-calendar-event"></i> Created: ${ new Date(feedback.created_at).toLocaleString() }</div>
                                <div class="mb-1 small"><i class="bi bi-calendar-event"></i> Updated: ${ feedback.updated_at ? new Date(feedback.updated_at).toLocaleString() : "Not yet" }</div>
                                <div class="mb-1 small"><i class="bi bi-database"></i> ID: ${ feedback.uuid }</div>
                            </div>
                        </a>
                    `)
            })
        })

    document.querySelector("#run-analysis").onclick = (e) => {
        axios.get(`/api/assessments/${assessment_uuid}/analyze`)
    }
})();