//project goals (provided by codecademy): In this project, you’ll be building an interactive terminal game. The scenario is that the player has lost their hat in a field full of holes, and they must navigate back to it without falling down one of the holes or stepping outside of the field.

//https://www.codecademy.com/practice/projects/find-your-hat

const prompt = require('prompt-sync')({sigint: true});

const hat = '^';
const hole = 'O';
const fieldCharacter = '░';
const pathCharacter = '*';

class Field {
    //field parameter should take array that consists of holes, one hat, and neutral background character
    constructor(field) {
        this._field = field;
    }

    //getter for field
    get field() {
        return this._field;
    }

    //setter for field
    set field(new_field) {
        this._field = new_field;
    }

    //prints field to the terminal in string formation 
    print() {
        this._field.forEach(element => {
            console.log(element.join(''));
        });
    }

    //method to start new game
    new_game() {
        console.log('Making your field!')
        this.moving()
    }
    

    //do do-while loop that takes user input in until valid input until hat found, loses by landing in hole, or moves outside field. Replace current position with *
    user_move() {
        const move_options = ['U', 'D', 'R', 'L'];
        let next_move = ""
        do {
            next_move = prompt(
                `What is your next move?
                U: up; D: Down; R: Right; L: Left  `)
        } while (move_options.includes(next_move) != true);
        return next_move
    }

    //method to move item and then  prompt another move until hat found, loses by landing in hole, or moves outside field. Replace current position with *
    moving(field = this._field, row = 0, column = 0) {
        this.print()
        let move = this.user_move();
        if (move == 'U') {
            row--;
        } if (move == 'D') {
            row++;
        } if (move == 'R') {
            column++;
        } if (move == 'L') {
            column--;
        } 
        
        if (this.field[row] == undefined || this.field[row][column] == undefined) {
            console.log('\nYou roamed out of the field! You Lost!')
            console.log('\nStarting new game.')
            this.new_game()
        }

        else if (this.field[row][column] == hat) {
            console.log('\nYou found your hat! You Win!')
            console.log('\nStarting new game.')
            this.new_game()
        } 
        
        else if (this.field[row][column] == hole) {
            console.log('\nYou fell in a hole! You Lost!')
            console.log('\nStarting new game.')
            this.new_game()
        }

        else if (this.field[row][column] == pathCharacter) {
            console.log('\nYou have already been there chose a new directions.')
            this.new_game()
        }

        else {
            this.field[row][column] = pathCharacter;
            this.moving(this.field, row, column);
        }

    }
    
    //static method for generating a field
    static generateField(height = 6, width = 4, difficulty = 'easy') {
        let percent_hole = 0;
        if (difficulty == 'easy') {
            percent_hole = 10;
        } if (difficulty == 'moderate') {
            percent_hole = 20;
        } if (difficulty == 'hard') {
            percent_hole = 30;
        }
        
        let new_field = [...Array(height)].map(e => Array(width))
        console.log(new_field.length)
        for (let i = 0; i < new_field.length; i++) {
            console.log(new_field[i])
            for (let j = 0; j < new_field[0].length; j++) {
            //new_field[i].map(element => {
                let rand_num = Math.floor(Math.random() * 100)
                console.log(rand_num)
                if (rand_num < percent_hole) {
                    new_field[i][j] = hole;
                } else {
                    new_field[i][j] = fieldCharacter;
                    //element = fieldCharacter;
                }
            }
        }
        new_field[0][0] = pathCharacter;
        let hat_row = Math.floor(Math.random() * (height- 1) + 1)
        let hat_column = Math.floor(Math.random() * width);
        new_field[hat_row][hat_column] = hat;
        return new_field
    }

}


const test = new Field([
    ['*', '░', '░'], 
    ['O', '░', '░'], 
    ['░', 'O', '░'], 
    ['░', '░', '░'], 
    ['░', '░', 'O'], 
    ['░', 'O', '░'], 
    ['░', '^', '░']
])

test_field = Field.generateField(12, 12, 'hard')

console.log(test_field)

test_1 = new Field(test_field)

test_1.new_game()