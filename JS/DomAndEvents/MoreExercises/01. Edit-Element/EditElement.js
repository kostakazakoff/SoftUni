function editElement(element, stringMatch, replacer) {
    element.textContent = element.textContent.split(stringMatch).join(replacer);
}