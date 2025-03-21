# Multi Use Case Example  

```MetaConfig
Definitions:
  94be: Combination Recommendation
  38a6: Category | Combination NoForm | lan-html, js
  4ddf: schemaID | lan-html, js
  a869: schemaID | lan-css
  b29c: themeID | lan-css

Instructions:
  94be:
    html:
      requires:
        id: 38a6
        requires: js
        recommended: a367::js
        compatible:
          - lan-js | NoForm | ~Post


---

## Fullstack Structure: Forms  

### HTML / JavaScript Form NoForm  

#### 66ab,94be,38a6,4ddf:: HTML Form: JavaScript  

~~~html
<div>
    <!-- iter:Start:Fields -->
    <label for="__FIELD_ID__">__FIELD_LABEL__:</label>
    <input type="__FIELD_TYPE__" id="__FIELD_ID__" name="__FIELD_NAME__" value="__FIELD_VALUE__" __FIELD_ATTRIB__ __FIELD_REQUIRED__>
    <!-- iter:End:Fields -->
    <button onclick="_.app.send()">Submit</button>
</div>
~~~

#### a367::38a6,4ddf:: JavaScript Form Post  

~~~js
_ = typeof _ !== 'undefined' ? _ : {};
_.v = typeof _.v !== 'undefined' ? _.v : {};

_.app = {
    send: function(callback) { 
        $.post(
            '__POST_URL__', {
                // iter:Start:Fields
                '__FIELD_NAME__': $('#__FIELD_ID__').val(),
                // iter:End:Fields
            },
            function(data) {
                if (typeof callback === 'function') {
                    callback(data);
                }
            }
        );
    },
};
~~~

---

## HTML Library  

#### bab6:: HTML Form Basic  

~~~html
<div>
    <form action="#" method="post">
        <!-- iter:Start:Fields -->
        <label for="__FIELD_ID__">__FIELD_LABEL__:</label>
        <input type="__FIELD_TYPE__" id="__FIELD_ID__" class="__FIELD_CLASS__" name="__FIELD_NAME__" value="__FIELD_VALUE__" __FIELD_ATTRIB__ __FIELD_REQUIRED__>
        <!-- iter:End:Fields -->
        <button type="submit">Submit</button>
    </form>
</div>
~~~

---

## CSS Library  

#### bbc1,a869:: CSS Style-Dependent Library Form | Core  

~~~css
:root {
    /* Prerequisite:Root-Formatting|Min */
    /* Root-Formatting|Supplemental */
    /* Prerequisite:Root-Theme */
}

input, select, textarea {
  width: 100%;
  padding: var(--padding);
  margin-bottom: var(--margin);
  border: 1px solid var(--input-border);
  border-radius: var(--border-radius);
  background-color: var(--input-bg);
  font-size: var(--font-size);
  color: var(--text-color);
  transition: 0.3s;
}

button {
  display: inline-block;
  width: 100%;
  padding: var(--padding);
  font-size: var(--font-size);
  background-color: var(--btn-bg);
  color: var(--btn-text);
  border: none;
  border-radius: var(--border-radius);
  cursor: pointer;
  transition: 0.3s;
}

button:hover {
  background-color: var(--btn-hover);
}
~~~

#### 9fe1,a869:: CSS Root-Formatting Library Form | Core  

~~~css
  --font-family: 'Arial', sans-serif;
  --font-size: 16px;
  --padding: 10px;
  --margin: 10px;
  --border-radius: 6px;
~~~

#### acf8,a869,b29c:: CSS Root-Theme | Dark  

~~~css
--dark-bg-color: #222;
--dark-text-color: #f1f1f1;
--dark-input-bg: #333;
--dark-input-border: #555;
--dark-input-focus: #1e90ff;
--dark-btn-bg: #1e90ff;
--dark-btn-hover: #1565c0;
~~~

#### 321b,a869,b29c:: CSS Root-Theme | Light  

~~~css
--bg-color: #f9f9f9;
--text-color: #333;
--input-bg: #fff;
--input-border: #ccc;
--input-focus: #007bff;
--btn-bg: #007bff;
--btn-text: #fff;
--btn-hover: #0056b3;
~~~

---

## Advanced API Integration  

### REST API (Express.js Backend with JWT Authentication)  

#### 11f3:: Express.js API - User Authentication  

~~~js
const express = require('express');
const jwt = require('jsonwebtoken');

const app = express();
app.use(express.json());

const users = [
    { id: 1, username: 'admin', password: 'password123', role: 'admin' }
];

// iter:Start:TokenGeneration
app.post('/login', (req, res) => {
    const { username, password } = req.body;
    const user = users.find(u => u.username === username && u.password === password);
    if (!user) return res.status(401).send('Invalid credentials');

    const token = jwt.sign({ id: user.id, role: user.role }, 'secretkey', { expiresIn: '1h' });
    res.json({ token });
});
// iter:End:TokenGeneration

app.listen(3000, () => console.log('Server running on port 3000'));
~~~

#### 2d77:: API Frontend Fetch Example

~~~js
async function authenticateUser(username, password) {
    const response = await fetch('http://localhost:3000/login', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ username, password })
    });

    if (!response.ok) throw new Error('Authentication failed');
    
    const { token } = await response.json();
    localStorage.setItem('authToken', token);
    console.log('User authenticated:', token);
}
~~~

---

## Complex SQL Queries for Reporting  

#### 99c4:: SQL Query - Multi-Join User & Orders Report

~~~sql
SELECT 
    users.id AS user_id, 
    users.name AS user_name, 
    orders.id AS order_id, 
    orders.total AS order_total, 
    payments.payment_status 
FROM users
INNER JOIN orders ON users.id = orders.user_id
LEFT JOIN payments ON orders.id = payments.order_id
WHERE users.status = 'active';

/* iter:Start:DateFilter */
AND orders.created_at >= '2024-01-01'
/* iter:End:DateFilter */
~~~

#### 0dd5:: SQL Query - Indexed Performance Optimization  

~~~sql
CREATE INDEX idx_users_id ON users(id);
CREATE INDEX idx_orders_user ON orders(user_id);
CREATE INDEX idx_payments_order ON payments(order_id);
~~~
