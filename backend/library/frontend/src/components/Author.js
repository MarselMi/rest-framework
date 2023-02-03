import React from 'react'
import {Link} from 'react-router-dom'

const AuthorItem = ({item}) => {
    return (
        <tr>
            <td><Link to={`author/${item.id}`}>{item.id}</Link></td>
            <td>{item.name}</td>
            <td>{item.birthday_year}</td>
        </tr>
    )
}


const AuthorList = ({items}) => {
    return (
        <table>
            <tr>
                <th>ID</th>
                <th>last name</th>
                <th>birthday year</th>
            </tr>
            {items.map((items) => <AuthorItem items={items} />)}
        </table>
    )
}


export default AuthorList