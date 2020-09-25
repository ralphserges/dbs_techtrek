const express = require('express'); //Import Express
const Joi = require('joi'); //Import Joi
const app = express(); //Create Express Application on the app variables
app.use(express.json()); // Because we using a json file with a list of data. Not using at mongo db etc.


//Give data to server
const customers = [

    //Data usually stored in server
    { title: 'George', id: 1},
    { title: 'Get', id: 2 },
    { title: 'orge', id: 3 },
    { title: 'rge', id: 4 },
    { title: 'Gee', id: 5 }
]


//Read request Handlers
//display the message when the URL consist of '/'

//After mentioning the URL ('/') can request and response are the parameters used in the GET method.
//Request is client side, response is server side
app.get('/', (req, res) => {
    res.send("Welcome to the API")
});

//Display the List of Customers when URL consists of api customers
app.get('/api/customers', (req, res) => {
    res.send(customers);
});






//Display the information of the specific customer when you mention the id.
app.get('/api/customers/:id', (req, res) => {
    const customer = customers.find(c => c.id == parseInt(req.params.id));

//If there are no valid customer ID, then display an error with the following message
if (!customer) res.status(404).send('<h2> Cant find what youre looking for</h2>');
res.send(customer);
});




//Create request handler
//Create new customer Information
app.post('/api/customers', (req, res) => {
    const { error } = validateCustomer(req.body);
    if (error) {
        res.status(400).send(error.details[0].message);
        return;
    }

    //Increment Customer id
    const customer = {
        id: customers.length + 1,
        title: req.body.title
    };


    customers.push(customer);
    //customer.title = req.body.title;
    res.send(customer);

});

//Update Request handler
//Update existing customer Information

app.put('/api/customers/:id', (req, res) => {

    const customer = customers.find(c => c.id === parseInt(req.params.id));
    //If there are no valid customer ID, then display an error with the following message
    if (!customer) res.status(404).send('<h2> Cant find what youre looking for</h2>');


    if (error) {
        res.status(400).send(error.details[0].message);
        return;
    }

    customer.title = req.body.title;

    //Customer object dated with new value and response sent back
    res.send(customer);
});


//Delete Request Handler
//Delete Customer Details
app.delete('/api/customers/:id', (req, res) => {

    const customer = customers.find(c => c.id === parseInt(req.params.id));

    //If there are no valid customer ID, then display an error with the following message
    if (!customer) res.status(404).send('<h2> Cant find what youre looking for</h2>');

    const index = customers.indexOf(customer);
    customers.splice(index, 1);


    res.send(customer);


});


//Validate Information
function validateCustomer(customer) {
    const schema = {
        title: Joi.string().min(3).required()
    };
    return Joi.validate(customer, schema);
}


//PORT Environment variable
//Server running here

const port = process.env.PORT || 8080;
app.listen(port, () => console.log('Listening on port ${port}.. '));


//or can try App.listen(3000);

