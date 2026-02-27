(function() {
    let personalInfo = {}

    document.querySelector("#form-submit-btn").onclick = () => {
        let clientForm = document.querySelector("#client-frm")

        if(clientForm.reportValidity()) {
            personalInfo["first_name"] = document.querySelector("#first_name").value
            personalInfo["middle_name"] = document.querySelector("#middle_name").value
            personalInfo["last_name"] = document.querySelector("#last_name").value
            personalInfo["ext_name"] = document.querySelector("#ext_name").value
            personalInfo["birth_date"] = document.querySelector("#birth_date").value
            personalInfo["sex"] = document.querySelector("#sex").value
            personalInfo["civil_status"] = document.querySelector("#civil_status").value
            personalInfo["email"] = document.querySelector("#email").value
            personalInfo["contact_number"] = document.querySelector("#contact_number").value
            personalInfo["philhealth_number"] = document.querySelector("#philhealth_number").value

            axios.post("/api/clients",
                personalInfo
            ).then(() => {
                alert("Client successfully added!")
                clientForm.reset()
            })
        }
    }
})();