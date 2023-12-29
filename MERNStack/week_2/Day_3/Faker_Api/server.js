
const express = require("express");
// console.log(express);
const app = express();
const PORT = 8000;
const { faker } = require('@faker-js/faker');
// make sure these lines are above any app.get or app.post code blocks
// ***MIDDLEWRAE***
app.use(express.json());
app.use(express.urlencoded({ extended: true }));

// ====================================================

// The import line will look different than what is in Faker's documentation
// because we are working with an express application

// we can create a function to return a random / fake "Product"
const createUser = () => {
    const newUser = {
        password: faker.internet.password(),
        email: faker.internet.email({ firstName, lastName }),
        phoneNumber: faker.phone.number(),
        lastName: faker.person.lastName(),
        firstName: faker.person.firstName(sex),
        _id: faker.database.mongodbObjectId(),



    };
    return newUser;
};

const createCompany = () => {
    const newCompany = {
        _id: faker.database.mongodbObjectId(),
        name: faker.company.name(),
        address: { 
            street: faker.location.streetAddress(), 
            city :faker.location.city(),
            zipCode:faker.location.zipCode(),
            state :faker.location.state(),
            country:faker.location.country(),
        },
    };
    return newFake;
};
    

//! POST - CREATE A USER
app.post("/api/users/new", (req, res) => {
  console.log(req.body);
  users.push(req.body);
  res.json(users);
});

//! POST - CREATE A company
app.post("/api/companies/new", (req, res) => {
  console.log(req.body);
  users.push(req.body);
  res.json(companies);
});

//! POST - CREATE A user and his company
app.post("/api/user/company", (req, res) => {
    console.log(req.body);
    users.push(req.body);
    res.json(user);
  });
  
  



// this needs to be below the other code blocks
app.listen(PORT, () => {
  console.log(`The server is up & running on PORT ${PORT}`);
});




