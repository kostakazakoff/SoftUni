function attachGradientEvents() {
    const gradient = document.getElementById('gradient');
    const output = document.getElementById('result');
    gradient.addEventListener('mousemove', detectMousePosition);
    gradient.addEventListener('mouseout', hideInfo);

    function detectMousePosition(e) {
        const sizeX = gradient.clientWidth;
        let mousePositionX = e.offsetX;
        let positionInPercent = Math.floor(mousePositionX * 100 / sizeX);
        output.textContent = `${positionInPercent}%`;
    }

    function hideInfo() {
        output.textContent = '';
    }
}