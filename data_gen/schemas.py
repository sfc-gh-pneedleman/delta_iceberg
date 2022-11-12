

CUSTOMERS_SCHEMA = [{
    "name": "CUSTOMER_NUM",
    "type": 'id'
}, {
    "name": "FIRST_NAME",
    "type": 'first_name'
}, {
    "name": "LAST_NAME",
    "type": "last_name"
}, {
    "name": "COMPANY",
    "type": "company"
}, {
    "name": "CITY",
    "type": "city",
}, {
    "name": "COUNTRY",
    "type": "country",
}, {
    "name": "PHONE_1",
    "type": "phone"
}, {
    "name": "PHONE_2",
    "type": "phone"
}, {
    "name": "EMAIL",
    "type": "business_email"
}, {
    "name": "DOB",
    "type": "date_of_birth"
}, {
    "name": "WEBSITE",
    "type": "website"
}]

TXN_SCHEMA = [{
    "name": "TRANSACTION_NUM",
    "type": 'id'
}, {
    "name": "TRANSACTION_DATE",
    "type": 'date_this_decade'
}, {
    "name": "UNIT_PRICE",
    "type": 'number'
}, 
{
    "name": "QUANTITY",
    "type": 'quantity'
}, 
{
    "name": "TRANSACTION_DESC",
    "type": 'company_desc'
},
{
    "name": "CUSTOMER_ID",
    "type": 'customer_id'
}]


ORGANIZATIONS_SCHEMA = [{
    "name": "Organization Id",
    "type": 'id'
}, {
    "name": "Name",
    "type": "company"
}, {
    "name": "Website",
    "type": "website"
}, {
    "name": "Country",
    "type": "country"
}, {
    "name": "Description",
    "type": "company_desc"
}, {
    "name": "Founded",
    "type": "year"
}, {
    "name": "Industry",
    "type": "industry"
}, {
    "name": "Number of employees",
    "type": "company_number_employees"
}]
