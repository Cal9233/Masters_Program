async function SubmitFn(button) {
    const ssn = document.getElementById("tb_ssn").value;
    const fname = document.getElementById("tb_fname").value;
    const lname = document.getElementById("tb_lname").value;
    const med = document.getElementById("tb_med").value;
    const dos = document.getElementById("tb_dos").value;

    disableButton(button);

    await GetPharmacyBenefits(ssn, fname, lname, med, dos).then(displayData);

    enableButton(button);
}

function displayData(data) {
    console.log(data);
    const text = dataToString(data);
    console.log(text);
    document.getElementById("ta_result").value = text;
}

function enableButton(button) {
    button.disabled = false;
}

function disableButton(button) {
    button.disabled = true;
}

async function GetPharmacyBenefits(ssn, fname, lname, med, dos) {
    const response = await fetch(`http://localhost:8000/pharmacy/v1/coverage?id=${ssn}&fname=${fname}&lname=${lname}&med=${med}&dose=${dos}`)
    const data = await response.json();
    return data;
}

function dataToString(data) {
    const cc = data.coverageClass;
    console.log(cc);
    const cp = parseInt(data.copay);
    console.log(cp);
    const oop = parseInt(data.outOfPocket);
    console.log(oop);
    const text =
        `Class: ${cc}`+'\n'+
        `Copay: \$${cp}`+'\n'+
        `Out of Pocket: \$${oop}`;
    return text;
}