(function() {
    axios.get(`/api/ai-feedback`)
        .then((response) => {
            let feedbacks = response.data

            feedbacks.forEach((feedback) => {
                document.querySelector("#feedback-list")
                    .insertAdjacentHTML("beforeend",`
                        <a href="/ai-feedback/${ feedback.uuid }" class="list-group-item list-group-item-action py-3 lh-tight">
                            <div class="d-flex w-100 align-items-start align-items-md-center justify-content-between flex-column flex-md-row">
                                <strong class="mb-1">AI Feedback #${ feedback.id } for Assessment #${ feedback.assessment.id }</strong>
                                <div class="mb-1 small"><i class="bi bi-star-fill"></i> Rating: ${ feedback.feedback_rating ? feedback.feedback_rating : "Not yet" }</div>
                            </div>
                            <div class="d-flex w-100 align-items-start align-items-md-center justify-content-between flex-column flex-md-row">
                                <div class="mb-1 small"><i class="bi bi-file-earmark-person"></i> Client: ${ feedback.assessment.client.first_name } ${ feedback.assessment.client.middle_name } ${ feedback.assessment.client.last_name }${ feedback.assessment.client.ext_name ? " " + feedback.assessment.client.ext_name : "" }</div>
                                <div class="mb-1 small"><i class="bi bi-database"></i> ID: ${ feedback.uuid }</div>
                            </div>
                            <div class="d-flex w-100 align-items-start align-items-md-center justify-content-between flex-column flex-md-row">
                                <div class="mb-1 small"><i class="bi bi-calendar-event"></i> Created: ${ new Date(feedback.created_at).toLocaleString() }</div>
                                <div class="mb-1 small"><i class="bi bi-calendar-event"></i> Updated: ${ feedback.updated_at ? new Date(feedback.updated_at).toLocaleString() : "Not yet" }</div>
                            </div>
                        </a>
                    `)
            })
        })
})();