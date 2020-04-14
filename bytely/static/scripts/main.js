$( ".full-link-td" ).each( function() {
    console.log($( this ).text());
    linkText = $( this ).text();
    if (linkText.length > 50) {
        console.log(1);
        $( this ).text(linkText.slice(0, 50) + "...");
    }
});    

const customLinkCheckbox = document.querySelector('input[name="want-custom-link"]');
const customLinkInput = document.querySelector('input[name="custom-link"]');
customLinkInput.style.display = "none";


customLinkCheckbox.addEventListener('change', () => {
    console.log(customLinkCheckbox.checked);
    if(customLinkCheckbox.checked) {
        customLinkInput.style.display = "inline-block";
    } else {
        customLinkInput.style.display = "none";
    }
});