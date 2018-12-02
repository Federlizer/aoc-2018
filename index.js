const fs = require("fs");
const solution = require("./dayone/solution");

fs.readFile("./dayone/input.txt", "utf8", (err, data) => {
    if (err) throw err;

    console.log(solution.chronicallyCalibratePT(data));
});