import React from 'react'
import { Link } from "react-router-dom"
import { Outlet } from "react-router-dom"

function Layout() {
  return (
    <div>

      <nav>
        <ul>
          <li>
            <Link to="/menu">Menu</Link>
          </li>

          <li>
            <Link to="/contact">Contact</Link>
          </li>


        </ul>
      </nav>

    <hr></hr>
      <Outlet/>
    </div>
  )
}

export default Layout