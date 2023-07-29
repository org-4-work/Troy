import React, { ReactNode } from 'react';
import { NavbarMinimalColored } from './Navbar';
import {Container,Skeleton,Grid,createStyles, rem   } from '@mantine/core';
interface LayoutProps {
  children: ReactNode;
}

const child = <Skeleton height={140} radius="md" animate={false} />;
const useStyles = createStyles((theme) => ({
    content: {
        position: 'relative',
        width : '100%'
      },

}));

const Layout: React.FC<LayoutProps> = ({ children }) => {
    const { classes, theme } = useStyles();
    return (
        <div style={{ display: 'flex', width: '100%' }}>
            <NavbarMinimalColored />
            <Container my="md" className={classes.content}>
                {children}
            </Container>
        </div>  
  );
};

export default Layout;
