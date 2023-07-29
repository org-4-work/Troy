import React from 'react';
import { BrowserRouter, Routes, Route } from "react-router-dom";
import { MantineProvider } from '@mantine/core';
import { ThemeProvider } from "./ThemeProvider";
import Layout from './layout/Layout'
import KfsDocument from './pages/KfsDocument'
import logo from './logo.svg';
import './App.css';

function App() {
  return (
    <ThemeProvider>
      <Layout>
        <BrowserRouter>
          <Routes>
            <Route path="/" element={<KfsDocument />} />
          </Routes>
        </BrowserRouter>
      </Layout>

    </ThemeProvider>

  );
}

export default App;
