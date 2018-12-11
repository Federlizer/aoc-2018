const fs = require("fs");
const solution = require("./daytwo/solution");

fs.readFile("./daytwo/input.txt", "utf8", (err, data) => {
    if (err) throw err;

    console.log(solution.manageInventory(data));
});