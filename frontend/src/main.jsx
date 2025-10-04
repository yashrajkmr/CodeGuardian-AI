import React from 'react';
import ReactDOM from 'react-dom/client';
import { MantineProvider } from '@mantine/core';
import App from './App.jsx';
import './index.css';

// We import the necessary CSS files for Mantine
import '@mantine/core/styles.css';

ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    {/* We wrap our App in the MantineProvider to make styles available */}
    <MantineProvider>
      <App />
    </MantineProvider>
  </React.StrictMode>,
);
