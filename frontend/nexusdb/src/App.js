 import './App.css';
// import DataTable from './DataTable.js'

// function App() {
//   return (
//     <body>
//     <div className="App">
//       <header className="App-header">
//       </header>
//       <h1>Welcome to NexusDB</h1>
//       <DataTable />
//     </div>
//     </body>
//   );
// }

// export default App;

// import React from 'react';
// import DataTable from './DataTable';

// const App = () => {
//     return (
//         <div style={{textAlign:'center'}}>
//             <h1>NexusDB</h1>
//             <div style={{ display: 'flex', justifyContent: 'center', marginLeft: '600px' }}>
//               <DataTable />
//             </div>
//         </div>
//     );
// };

// export default App;

import React, { useState, useEffect } from 'react';
import DataTable from './DataTable'; // Assuming CarTable.js is in the same directory

function App() {
    const [cars, setCars] = useState([]);

    useEffect(() => {
        fetchCars();
    }, []);

    const fetchCars = () => {
        fetch('/cars')
            .then(response => {
                if (!response.ok) {
                    throw new Error('Network response was not ok');
                }
                return response.json();
            })
            .then(data => {
                setCars(data);
            })
            .catch(error => {
                console.error('Error fetching data:', error);
            });
    };

    return (
        <div style={{ display: 'flex', justifyContent: 'center', marginLeft: '600px' }}>
            <DataTable />
        </div>
    );
}

export default App;

