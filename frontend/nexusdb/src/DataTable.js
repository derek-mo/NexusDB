import React, { useState, useEffect } from 'react';

const CarTable = () => {
    const [cars, setCars] = useState([]);

    useEffect(() => {
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
    }, []);

    return (
        <div>
            <h2>Car Table</h2>
            <table>
                <thead>
                    <tr>
                        <th>ID</th>
                        <th>Make</th>
                        <th>Model</th>
                        <th>Year</th>
                        <th>Price</th>
                    </tr>
                </thead>
                <tbody>
                    {cars.map(car => (
                        <tr>
                            <td>{car[0]}</td>
                            <td>{car[1]}</td>
                            <td>{car[2]}</td>
                            <td>{car[3]}</td>
                            <td>{car[4]}</td>
                        </tr>
                    ))}
                </tbody>
            </table>
        </div>
    );
};

export default CarTable;

