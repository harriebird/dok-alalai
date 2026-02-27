(function() {
    axios.get(`/api/clients/${client_uuid}`)
        .then((response) => {
            document.querySelector("#personal-info").disabled = true
            let clientInfo = response.data
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
        })

    axios.get(`/api/clients/${client_uuid}/assessments`)
        .then((response) => {
            let assessments = response.data

            assessments.forEach((assessment) => {
                document.querySelector("#assess-list")
                    .insertAdjacentHTML("beforeend",`
                        <a href="/assessments/${ assessment.uuid }" class="list-group-item list-group-item-action py-3 lh-tight">
                            <div class="d-flex w-100 align-items-center justify-content-between">
                                <strong class="mb-1">Assessment #${ assessment.id }: ${ assessment.client.first_name } ${ assessment.client.middle_name } ${ assessment.client.last_name }${ assessment.client.ext_name ? " " + assessment.client.ext_name : "" }</strong>
                            </div>
                            <div class="d-flex w-100 align-items-start align-items-md-center justify-content-between flex-column flex-md-row">
                                <div class="mb-1 small"><i class="bi bi-calendar-event"></i> Created: ${ new Date(assessment.created_at).toLocaleString() }</div>
                                <div class="mb-1 small"><i class="bi bi-rainbow"></i> AI Feedback: ${ assessment.feedback.length }</div>
                                <div class="mb-1 small"><i class="bi bi-database"></i> ID: ${ assessment.uuid }</div>
                            </div>
                        </a>
                    `)
            })
        })

    document.querySelector("#edit-btn").onclick = (e) => {
        e.preventDefault()

        document.querySelector("#personal-info").disabled = false
    }
})();