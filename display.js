class Display {
    constructor(value) {
        this.display_element = document.getElementById("display");
        this.value = value;
        this.display = [];

        this.display_element.innerHTML = ""; // Clear previous display
    }

    getLenght() {
        let length = 0;
        let value = this.value;

        while(value >= 0) {
            value = Math.floor(value / 10);
            length++;

            if(value == 0) {
                break;
            }
        }

        return length;
    }

    buildDisplay() {
        const display_count = this.getLenght();
        const display_dim = {
            "width": 5*display_count-(display_count-1),
            "height": 7
        }

        //Create display array
        for(var i = 0; i < display_dim["height"]; i++) {
            this.display.push([]);
            for(var j = 0; j < display_dim["width"]; j++) {
                this.display[i].push(0);
            }
        }

        //Create display
        const table = document.createElement("table");
        for(var i = 0; i < display_dim["height"]; i++) {
            const row = document.createElement("tr");
            for(var j = 0; j < display_dim["width"]; j++) {
                const cell = document.createElement("td");
                cell.className = "off";
                cell.id = `${i}-${j}`;
                row.appendChild(cell);
            }
            table.appendChild(row);
        }
        this.display_element.appendChild(table);
    }

    drawDigit(n, display_number) {
        const delta = 4 * (display_number - 1);

        // Helper functions use arrow syntax to preserve 'this'
        const top_horizontal = () => {
            for (let i = 1; i <= 3; i++) {
                this.display[1][i + delta] = 1;
            }
        };

        const middle_horizontal = () => {
            for (let i = 1; i <= 3; i++) {
                this.display[3][i + delta] = 1;
            }
        };

        const bottom_horizontal = () => {
            for (let i = 1; i <= 3; i++) {
                this.display[5][i + delta] = 1;
            }
        };

        const top_left_vertical = () => {
            for (let i = 1; i <= 3; i++) {
                this.display[i][1 + delta] = 1;
            }
        };

        const top_right_vertical = () => {
            for (let i = 1; i <= 3; i++) {
                this.display[i][3 + delta] = 1;
            }
        };

        const bottom_left_vertical = () => {
            for (let i = 3; i <= 5; i++) {
                this.display[i][1 + delta] = 1;
            }
        };

        const bottom_right_vertical = () => {
            for (let i = 3; i <= 5; i++) {
                this.display[i][3 + delta] = 1;
            }
        };

        // Draw digital digit
        switch (n) {
            case 0:
                top_horizontal();
                bottom_horizontal();
                top_left_vertical();
                top_right_vertical();
                bottom_left_vertical();
                bottom_right_vertical();
                break;
            case 1:
                top_right_vertical();
                bottom_right_vertical();
                break;
            case 2:
                top_horizontal();
                middle_horizontal();
                bottom_horizontal();
                top_right_vertical();
                bottom_left_vertical();
                break;
            case 3:
                top_horizontal();
                middle_horizontal();
                bottom_horizontal();
                top_right_vertical();
                bottom_right_vertical();
                break;
            case 4:
                top_left_vertical();
                middle_horizontal();
                top_right_vertical();
                bottom_right_vertical();
                break;
            case 5:
                top_horizontal();
                middle_horizontal();
                bottom_horizontal();
                top_left_vertical();
                bottom_right_vertical();
                break;
            case 6:
                top_horizontal();
                middle_horizontal();
                bottom_horizontal();
                top_left_vertical();
                bottom_left_vertical();
                bottom_right_vertical();
                break;
            case 7:
                top_horizontal();
                top_right_vertical();
                bottom_right_vertical();
                break;
            case 8:
                top_horizontal();
                middle_horizontal();
                bottom_horizontal();
                top_left_vertical();
                top_right_vertical();
                bottom_left_vertical();
                bottom_right_vertical();
                break;
            case 9:
                top_horizontal();
                middle_horizontal();
                bottom_horizontal();
                top_left_vertical();
                top_right_vertical();
                bottom_right_vertical();
                break;
        }

        // Update display
        for (let i = 0; i < this.display.length; i++) {
            for (let j = 0; j < this.display[i].length; j++) {
                const cell = document.getElementById(`${i}-${j}`);
                if (cell) {
                    cell.className = this.display[i][j] === 1 ? "on" : "off";
                }
            }
        }
    }

    drawNumber() {
        let value = this.value;
        let l = []

        while(value >= 0) {
            l.push(value % 10); //List stores digits in reverse order
            value = Math.floor(value / 10);
            if(value == 0) {
                break;
            }
        }

        for(var i = l.length-1; i > -1; i--) {
            this.drawDigit(l[i], l.length-i);
        }
    }
}


const numberInput = document.getElementById("numberInput");
numberInput.addEventListener("input", function() {
    const value = parseInt(numberInput.value);
    if (!isNaN(value)) {
        let user_val = new Display(value);
        user_val.buildDisplay();
        user_val.drawNumber();
    }
});
