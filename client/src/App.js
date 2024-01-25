import { Routes, Route } from "react-router-dom"
import Layout from "./Layout"
import Contact from "./Contact"
// import Menu from "./menu" 
import Menu from './menu'
import NOTFOUND from "./not_found"

function App() {
  return (
    <div>

      <h1>Routes</h1>
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