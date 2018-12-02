const fs = require("fs");
const solution = require("./dayone_solution");

fs.readFile("dayone_input.txt", "utf8", (err, data) => {
    if (err) throw err;

    console.log(solution.chronicallyCalibratePT(data));
});