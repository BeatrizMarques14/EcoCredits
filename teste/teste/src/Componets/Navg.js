import React, { useState} from "react";
import { Link } from "react-router-dom";
import './Navg.css';


function Navg() {
  const [click, setClick] = useState(false);
   const handleClick = () => setClick(!click);
  const closeMobileMenu = () =>setClick(false);
 
  return (
    <>
      <nav className='navbar'>
        <div className='navbar-container'>
          <Link to="/" className='navbar-logo' onClick={closeMobileMenu}>
           EcoCredits < i/>
          
          </Link>
          <div className='menu-icon' onClick={handleClick}>
            <i className={click ? 'fas fa-times' : 'fas fa-bars'} />
          </div>
          <ul className={click ? 'nav-menu active' : 'nav-menu'}>
            <li classname ='nav-item'>
            <Link to='/' className='nav-links'  onClick={closeMobileMenu}>
                Home
            </Link> 
            </li>
            <li classname ='nav-item'>
            <Link to='/Precos' className='nav-links'  onClick={closeMobileMenu}>
                Pontos
            </Link> 
            </li>
          </ul>
         
        </div>
      </nav>
    </>
  );
}

export default Navg;
