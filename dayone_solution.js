exports.chronicallyCalibrate = (input) => {
    let frequencyChanges = input.split("\n");
    let frequency = 0;

    for (let frequencyChange of frequencyChanges) {
        frequency = calibrate(frequency, frequencyChange)
    }
    
    return frequency;
};

exports.chronicallyCalibratePT = (input) => {
    let frequencyChanges = input.split("\n");
    let frequency = 0;
    let seenChange = [0];

    let found = false;
    let i = 0;

    while(!found) {
        let frequencyChange = frequencyChanges[i];

        frequency = calibrate(frequency, frequencyChange);

        for (let j = 0; j < seenChange.length - 1; j++)
            if (seenChange[j] === frequency)
                return frequency;

        seenChange.push(frequency);
        if (i === frequencyChanges.length - 1)
            i = 0;
        else
            i++;
    }
};

function calibrate(currentFrequency, command) {
    if (command.substring(0, 1) === "+") {
        return currentFrequency + Number(command.substring(1));
    } else {
        return currentFrequency - Number(command.substring(1));
    }
}