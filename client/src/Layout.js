import React from 'react';
import { Link } from 'react-router-dom';
import { Outlet } from 'react-router-dom';

import 'bootstrap/dist/css/bootstrap.min.css';
import 'bootstrap/dist/js/bootstrap.min.js';

function Layout() {
  return (
    <div className='mx-auto'>
<nav className="navbar navbar-expand-lg bg-body-tertiary justify-content-center position-absolute top-0 start-50 translate-middle-x">
        <div className="container-fluid mx-auto">
          <Link className="navbar-brand " to="/" style={{marginRight: '5rem'}}>
            Logo
          </Link>
          <button
            className="navbar-toggler"
            type="button"
            data-bs-toggle="collapse"
            data-bs-target="#navbarNavDropdown"
            aria-controls="navbarNavDropdown"
            aria-expanded="false"
            aria-label="Toggle navigation"
          >
            <span className="navbar-toggler-icon"></span>
          </button>
          <div className="collapse navbar-collapse" id="navbarNavDropdown">
            <ul className="navbar-nav">
              {/* <li className="nav-item">
                <Link className="nav-link active " to="/dashboard" style={{marginRight: '5rem'}}>
                  Dashboard
                </Link>
              </li> */}
              <li className="nav-item">
                <Link className="nav-link active " to="/categories" style={{marginRight: '5rem'}}>
                  Categories
                </Link>
              </li>
              <li className="nav-item">
                <Link className="nav-link active" to="/roles" style={{marginRight: '5rem'}}>
                  Roles
                </Link>
              </li>
              
              <li className="nav-item">
                <Link className="nav-link active " to="/contact" style={{marginRight: '5rem'}}>
                  Contact
                </Link>
              </li>
              <li className="nav-item">
                <Link className="nav-link active " to="/about-us" style={{marginRight: '5rem'}}>
                  About us
                </Link>
              </li>
              {/* <li className="nav-item dropdown"> When logged in, this to "My Account"
                <Link
                  className="nav-link dropdown-toggle "
                  to="#"
                  role="button"
                  data-bs-toggle="dropdown"
                  aria-expanded="false"
                >
                  Dropdown link
                </Link>
                <ul className="dropdown-menu">
                  <li>
                    <Link className="dropdown-item" to="#">
                      Action
                    </Link>
                  </li>
                  <li>
                    <Link className="dropdown-item" to="#">
                      Another action
                    </Link>
                  </li>
                  <li>
                    <Link className="dropdown-item" to="#">
                      Something else here
                    </Link>
                  </li>
                </ul>
              </li> */}
            </ul>
          </div>
        </div>
      </nav>

      <Outlet />
    </div>
  );
}

export default Layout;
