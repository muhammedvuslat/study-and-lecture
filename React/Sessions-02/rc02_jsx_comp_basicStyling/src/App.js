import React from "react";
import Footer from "./components/Footer";
import Header from "./components/Header";
//! Componentler, HTML,CSS ve JS kodlarindan meydana gelmiş
//! bir kod parcacigidir.
//! Bir componentin return () kismi ise JSX kodlari icerir.
//! JSX'in kendine gore bazi kurallari vardir. Ornegin bir
//! component eger birden fazla html elementi dondurmesi
//! gerekirse bunlari tek bir container elemani ile sarmayalarak
//! dondurmelidir.container icin div, article, header, <> v.b
//! herhangi bir element kullanilabilir.

function App() {
  return (
    <>
      <Header />
      <Footer />
    </>
  );
}

export default App;
