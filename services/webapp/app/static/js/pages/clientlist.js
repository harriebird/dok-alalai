(function() {

    let clients = []

    axios.get("/api/clients")
        .then((response)=> {
            let clients = response.data

            clients.forEach((client) => {
                document.querySelector("#client-list")
                    .insertAdjacentHTML("beforeend",`
                        <a href="/clients/${ client.uuid }" class="list-group-item list-group-item-action py-3 lh-tight">
                            <div class="d-flex w-100 align-items-center justify-content-between">
                                <strong class="mb-1">${ client.first_name } ${ client.middle_name } ${ client.last_name }${ client.ext_name ? " " + client.ext_name : "" }</strong>
                                ${ client.contact_number ? '<small class="text-muted"><i class="bi bi-telephone-fill"></i> ' + client.contact_number + '</small>' : ""}
                            </div>
                            <div class="d-flex w-100 align-items-center justify-content-between">
                                <div class="mb-1 small">${ client.sex === "Male" ? '<i class="bi bi-gender-male"></i>' : '<i class="bi bi-gender-female"></i>'} Sex: ${ client.sex }</div>
                                <div class="mb-1 small"><i class="bi bi-person-hearts"></i> Civil Status: ${ client.civil_status }</div>
                            </div>
                            <div class="d-flex w-100 align-items-center justify-content-between">
                                <div class="mb-1 small"><i class="bi bi-balloon"></i> Age: ${ Math.abs((new Date(Date.now() - new Date(client.birth_date).getTime())).getFullYear() - 1970) }</div>
                                <div class="mb-1 small"><i class="bi bi-cake2"></i> Birthday: ${ new Date(client.birth_date).toLocaleDateString('en-US') }</div>
                            </div>
                        </a>
                    `)
            })
        })
})();