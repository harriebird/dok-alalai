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
    return weight / ((height/100) ** 2);
}