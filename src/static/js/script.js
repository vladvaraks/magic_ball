function hiddenBtn(input, btn)
{
    input.addEventListener('input', function(event) {
        if (this.value == '') {
            btn.setAttribute("hidden", 'true');
        }
        else {
            btn.removeAttribute("hidden");
        }
    })
}