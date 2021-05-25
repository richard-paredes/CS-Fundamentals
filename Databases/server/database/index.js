const fs = require('fs');
const Pool = require('pg').Pool;
const Query = require('pg').Query;
const submit = Query.prototype.submit;

let isTransacting = false;
fs.writeFile('./database/sql/transact.sql', '', () => { })
fs.writeFile('./database/sql/query.sql', '', () => { })
Query.prototype.submit = function () {
  const text = this.text;
  const values = this.values || [];
  const query = text.replace(/\$([0-9]+)/g, (m, v) => JSON.stringify(values[parseInt(v) - 1]))

  if (query.includes('BEGIN;')) {
    isTransacting = true;
  }
  if (isTransacting) {
    fs.appendFile('./database/sql/transact.sql', query, () => {
      if (query.includes('COMMIT;') || query.includes('ROLLBACK;')) {
        isTransacting = false;
      }
    });
  } else {
    fs.appendFile('./database/sql/query.sql', query, () => {
    });
  }
  submit.apply(this, arguments);

};

try {
  var credentials = fs.readFileSync('./database/config/password.txt').toString().split("\n").map(x => x.trim());
  const pool = new Pool({
    host: 'code.cs.uh.edu',
    user: credentials[0],
    password: credentials[1],
    // user: 'postgres',
    // password: 'postgres',
    port: 5432,
    database: 'COSC3380'
  });

  pool.connect((err, client) => {
    if (err) {
      console.log('Failed to establish database connection. Ensure credentials are valid in password.txt.');
    } else {
      client.release();
    }
  });
  module.exports = pool;
} catch (err) {
  console.log('Password.txt file missing or invalid. Add password.txt file to server/database/config')
}