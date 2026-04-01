(function() {

    let toddler;
    let clientInfo;
    let medicalHistory = [];

    let yesNoQuestions = [2, 3, 4, 5, 6, 8, 9, 10]
    yesNoQuestions.forEach((number) => {
        document.querySelector(`#q${number}-yes`).onclick = (e) => {
            document.querySelector(`#question${number}`).classList.remove("d-none")
        }

        document.querySelector(`#q${number}-no`).onclick = (e) => {
            document.querySelector(`#question${number}`).classList.add("d-none")
        }
        })

    axios.get(`/api/clients/${client_uuid}`)
        .then((response) => {
            clientInfo = response.data

            toddler = getAgeMonths(clientInfo.birth_date) <= 24

            document.querySelector("#personal-info").disabled = true
            document.querySelector("#first_name").value = clientInfo.first_name
            document.querySelector("#middle_name").value = clientInfo.middle_name
            document.querySelector("#last_name").value = clientInfo.last_name
            document.querySelector("#ext_name").value = clientInfo.ext_name
            document.querySelector("#birth_date").value = clientInfo.birth_date
            document.querySelector("#sex").value = clientInfo.sex
            document.querySelector("#civil_status").value = clientInfo.civil_status
            document.querySelector("#email").value = clientInfo.email
            document.querySelector("#contact_number").value = clientInfo.contact_number
            document.querySelector("#philhealth_number").value = clientInfo.philhealth_number

            if(clientInfo.sex === "Male") {
                document.querySelector("#female-only").classList.add("d-none")
            }

            if(toddler) {
                document.querySelector("#for-toddler-frm").classList.remove("d-none")
            }
        })

    const input = document.querySelector("#med-hist-input");
    const container = document.querySelector("#med-hist-container");

    input.addEventListener("keydown", (e) => {
        if (e.key === "Enter" || e.key === ",") {
            e.preventDefault()
            const value = input.value.trim().replace(",", "")

            if (value && medicalHistory.indexOf(value) < 0) {
                addConditionBadge(value, container, input)
                medicalHistory.push(value)
            }
        }
    })

    container.addEventListener("click", () => input.focus())

    let handleBMI = function () {
        document.querySelector("#bmi").value = computeBMI(
            document.querySelector("#weight").value,
            document.querySelector("#height").value
        )
    }

    document.querySelector("#weight").onchange = handleBMI
    document.querySelector("#height").onchange = handleBMI

    document.querySelector("#form-submit-btn").onclick = () => {
        let assessData = {}
        let forms = []
        let validForms = []

        forms.push(document.querySelector("#systems-review-frm"))
        forms.push(document.querySelector("#social-history-frm"))
        forms.push(document.querySelector("#physical-exam-frm"))

        if(toddler) {
            forms.push(document.querySelector("#for-toddler-frm"))
        }

        forms.forEach((form) => {
            validForms.push(form.reportValidity())
        })
        assessData["assessment"] = {}
        assessData["medical_history"] = []
        assessData["physical_exam"] = {}

        if(toddler) {
            assessData["toddler_exam"] = {}
        }


        if(!validForms.includes(false)) {

            if (clientInfo.sex === "Male") {
                assessData["assessment"]["question7a"] = null
                assessData["assessment"]["question7b"] = null
                assessData["assessment"]["question7c"] = null
            } else {
                assessData["assessment"]["question7a"] = document.querySelector("#question7a").value
                assessData["assessment"]["question7b"] = document.querySelector("#question7b").value
                assessData["assessment"]["question7c"] = document.querySelector("#question7c").value
            }

            yesNoQuestions = [2, 3, 4, 5, 6, 8]
            yesNoQuestions.forEach((number) => {
                assessData["assessment"][`question${number}`] =
                    document.querySelector(`input[name="q${number}-ans"]:checked`).value === "yes" ?
                        document.querySelector(`#question${number}`).value : null
            })
            assessData["assessment"]["question1"] = document.querySelector("#question1").value
            assessData["assessment"]["smoke_years"] =
                    document.querySelector(`input[name="q9-ans"]:checked`).value === "yes" ?
                        document.querySelector(`#question9`).value : null
            assessData["assessment"]["alcohol_years"] =
                    document.querySelector(`input[name="q10-ans"]:checked`).value === "yes" ?
                        document.querySelector(`#question10`).value : null

            assessData["physical_exam"]["bp_systolic"] = document.querySelector("#bp_systolic").value
            assessData["physical_exam"]["bp_diastolic"] = document.querySelector("#bp_diastolic").value
            assessData["physical_exam"]["blood_type"] = document.querySelector("#blood_type").value
            assessData["physical_exam"]["heart_rate"] = document.querySelector("#heart_rate").value
            assessData["physical_exam"]["respiration_rate"] = document.querySelector("#respiration_rate").value
            assessData["physical_exam"]["va_top"] = document.querySelector("#va_top").value
            assessData["physical_exam"]["va_bottom"] = document.querySelector("#va_bottom").value
            assessData["physical_exam"]["height"] = document.querySelector("#height").value
            assessData["physical_exam"]["weight"] = document.querySelector("#weight").value
            assessData["physical_exam"]["temperature"] = document.querySelector("#temperature").value
            assessData["physical_exam"]["gen_survey"] = document.querySelector("#gen_survey").value
            assessData["physical_exam"]["additional_notes"] = document.querySelector("#additional_notes").value

            if(toddler) {
                assessData["toddler_exam"]["length"] = document.querySelector("#length").value
                assessData["toddler_exam"]["body_waist_circ"] = document.querySelector("#body_waist_circ").value
                assessData["toddler_exam"]["mid_upper_arm_circ"] = document.querySelector("#mid_upper_arm_circ").value
                assessData["toddler_exam"]["head_circ"] = document.querySelector("#head_circ").value
                assessData["toddler_exam"]["hip"] = document.querySelector("#hip").value
                assessData["toddler_exam"]["skinfold_thick"] = document.querySelector("#skinfold_thick").value
                assessData["toddler_exam"]["limbs"] = document.querySelector("#limbs").value
            }

            if(medicalHistory) {
                assessData["medical_history"] = medicalHistory
            }


            axios.post(`/api/clients/${client_uuid}/assess`,
                assessData
            ).then(()=> {
                alert("Assessment was successfully submitted!")
                window.location.href = `/clients/${client_uuid}`
            })
        }
    }

})();