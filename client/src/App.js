import { Routes, Route } from "react-router-dom"
import Layout from "./Layout"
import Contact from "./Contact"
import About_us from "./About-us"
import Roles from "./Roles"
import Categories from "./Categories"
// import Menu from "./menu" 
import Menu from './menu'
import NOTFOUND from "./not_found"
import "./navbar.css"

function App() {
  return (
    <div className="" style={{marginTop: '6rem', marginLeft: '3rem', marginRight: '3rem'}}>
    {/* // <div className="NavBar">

    //   <h1>Routes</h1> */}
      <Routes>
        <Route path="/" element={<Layout/>} >
          {/* <Route path="/dashboard" element={<Menu/>}></Route> */}
          <Route path="/contact" element={<Contact/>}></Route>
          <Route path="/categories" element={<Categories/>}></Route>
          <Route path="/roles" element={<Roles/>}></Route>
          <Route path="/about-us" element={<About_us/>}></Route>
          <Route path="*" element={<NOTFOUND/>}></Route>

        </Route>
      </Routes>


    </div>

  )
}

export default App