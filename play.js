var name = 'Max';
var age = 29;
var hasHobbies = true;

function summariseUser(userName, userAge, userhasHobby) {
    return (
        'Name is ' +
        userName +
        ', age is ' +
        userAge +
        ' and the user has hobbies ' +
        userhasHobby
    );
}

console.log(summariseUser(name, age, hasHobbies));

//console.log(name);