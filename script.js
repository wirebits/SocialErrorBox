// JavaScript File for SocialErrorBox
// Author - WireBits

function generateScript() {
    const variable = document.getElementById('setVariableArea').value;
    const title = document.getElementById('titleArea').value;
    const message = document.getElementById('messageArea').value;
    const icon = document.getElementById('iconSelect').value;
    const scriptButton = document.getElementById('buttonSelect').value;
    const finiteLoopValue = document.getElementById('finiteloopArea').value;
    const infiniteLoopValue = document.getElementById('infiniteSelect').value;
    const codeVariable = document.getElementById('setOtherVariableArea').value;
    const runCommand = document.getElementById('runArea').value;
	const buttonConst = document.getElementById('buttonConstSelect').value;

    let output = '';

    if (codeVariable && runCommand) {
        output += `Dim ${codeVariable}\n`;
        output += `Set ${codeVariable} = WScript.CreateObject("WScript.Shell")\n`;
        output += `${variable} = MsgBox("${message}", ${scriptButton} + ${icon}, "${title}")\n`;
        output += `If ${variable} = ${buttonConst} Then\n`;
        output += `    ${codeVariable}.Run "${runCommand}", 1, True\n`;
        output += `End If\n`;
    } else {
        if (infiniteLoopValue === 'Yes') {
            output += `Do\n    ${variable} = MsgBox("${message}", ${scriptButton} + ${icon}, "${title}")\nLoop`;
        } else if (finiteLoopValue && !isNaN(finiteLoopValue) && finiteLoopValue > 0) {
            output += `For i = 1 to ${finiteLoopValue}\n    ${variable} = MsgBox("${message}", ${scriptButton} + ${icon}, "${title}")\nNext`;
        } else {
            output += `${variable} = MsgBox("${message}", ${scriptButton} + ${icon}, "${title}")`;
        }
    }
    document.getElementById('outputArea').value = output;
}

function resetAll() {
    document.querySelectorAll('.textareaWrapper textarea').forEach(function(textarea) {
        textarea.value = '';
    });

    document.querySelector('#iconSelect').value = '';
    document.querySelector('#buttonSelect').value = '';
    document.querySelector('#infiniteSelect').value = '';

    document.querySelector('#finiteloopArea').value = '';
	document.querySelector('#buttonConstSelect').value = '';
}

window.onload = function() {
    document.querySelector('.reset').addEventListener('click', resetAll);
}

function saveFile() {
    var content = document.getElementById("outputArea").value;
    var blob = new Blob([content], { type: "text/plain;charset=utf-8" });
    var link = document.createElement("a");
    link.href = URL.createObjectURL(blob);
    link.download = "code.vbs";
    link.click();
}