function getAgeMonths(date) {
    const birthday = new Date(date)
    const today = new Date()

    let months = (today.getFullYear() - birthday.getFullYear()) * 12;
    months -= birthday.getMonth();
    months += today.getMonth();

    if (today.getDate() < birthday.getDate()) {
        months--
    }

    return months
}

function computeBMI(weight, height) {
    return (weight / ((height/100) ** 2)).toFixed(2);
}

function addConditionBadge(value, container, input) {
    const badge = document.createElement("span")
    badge.className = "badge bg-primary d-flex align-items-center p-2"
    badge.innerHTML = `${value} <button type="button" class="btn-close btn-close-white ms-2" style="font-size: 0.5rem;" aria-label="Close"></button>`

    badge.querySelector(".btn-close").addEventListener("click", () => {
        badge.remove()
        medicalHistory.splice(medicalHistory.indexOf(badge.innerText.trim()), 1)
    })

    container.insertBefore(badge, input)

    input.value = ""
}