function pyramidResources(side, increment){
    let step = 0;
    let stone = 0;
    let marble = 0;
    let lapisLazuli = 0;
    let gold = 0;
    let stepInnerMaterial = 0;
    let stepOuterMaterial = 0;
    let top = false;
    
    // BUILD
    while (side > 0){
        let fifthStep = false;
        step++;

        // define TOP of pyramid
        if (side - 2 <= 0){
            top = true;
        };

        // define 5th step
        if (step % 5 === 0 && !top){
            fifthStep = true;
        };

        // Calc level materials
        stepInnerMaterial = (side - 2)**2 * increment;
        stepOuterMaterial = (4 * side - 4) * increment;

        if (top){ //top
            gold += stepInnerMaterial + stepOuterMaterial;

        } else if (fifthStep){ // 5th step
            stone += stepInnerMaterial;
            lapisLazuli += stepOuterMaterial;

        } else { //regular step
            stone += stepInnerMaterial;
            marble += stepOuterMaterial;
        };

        // Reduce SIDE
        side -= 2;
    };
    let finalPyramidHeight = Math.floor(step * increment);
    console.log(`Stone required: ${Math.ceil(stone)}`);
    console.log(`Marble required: ${Math.ceil(marble)}`);
    console.log(`Lapis Lazuli required: ${Math.ceil(lapisLazuli)}`);
    console.log(`Gold required: ${Math.ceil(gold)}`);
    console.log(`Final pyramid height: ${finalPyramidHeight}`);
}

// pyramidResources(23,
//     0.5)