(function() {
    axios.get(`/api/assessments`)
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
})();