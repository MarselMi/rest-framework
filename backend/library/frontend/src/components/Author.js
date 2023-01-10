import React from 'react'


const AuthorItem = ({author}) => {
    return (
        <tr>
            <td>
                {author.email}
            </td>
            <td>
                {author.username}
            </td>
            <td>
                {author.firstname}
            </td>
            <td>
                {author.lastname}
            </td>
        </tr>
    )
}


const AuthorList = ({authors}) => {
    return (
        <table>
            <th>
                Email
            </th>
            <th>
                User name
            </th>
            <th>
                First name
            </th>
            <th>
                Last Name
            </th>
            {authors.map((author) => <AuthorItem author={author} />)}
        </table>
    )
}


export default AuthorList