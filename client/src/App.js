import { Routes, Route } from "react-router-dom"
import Layout from "./Layout"
import Contact from "./Contact"
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
          <Route path="/menu" element={<Menu/>}></Route>
          <Route path="/contact" element={<Contact/>}></Route>
          <Route path="*" element={<NOTFOUND/>}></Route>

        </Route>
      </Routes>


    </div>

  )
}

export default App