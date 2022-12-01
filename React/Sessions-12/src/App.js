import Footer from "./components/Footer";
import Nav from "./components/Nav";
import Contact from "./pages/Contact";
import Home from "./pages/Home";
import People from "./pages/People";
import NotFound from "./pages/NotFound";
import { Routes, Route } from "react-router-dom";
import Paths from "./pages/Paths";
import PersonDetail from "./pages/PersonDetail";

function App() {
  return (
    //! BrowserRoter a index çerisinde app i sarmaladğımız için gerek kalmadı
    <>
      <Nav />
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/people" element={<People />} />
        <Route path="/paths" element={<Paths />} />
        <Route path="/contact" element={<Contact />} />
        <Route path="/people/:id" element={<PersonDetail />} />
        <Route path="*" element={<NotFound />} />
      </Routes>

      <Footer />
    </>
  );
}

export default App;
