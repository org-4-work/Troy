import { Button, Menu, Text, useMantineTheme,Notification  } from '@mantine/core';
import { notifications } from '@mantine/notifications';
import apiUrl from "./../../config/api.js";
import axios from 'axios';
import {
  IconSquareCheck,
  IconChevronDown,
} from '@tabler/icons-react';

export function ButtonMenu() {
  const theme = useMantineTheme();

  const onDownload = async () => {
    try {
      const response = await axios.get(`${apiUrl}/api/download`, {
        headers: {
          'Content-Type': 'multipart/form-data'
        }
      });
      // console.log(response.data); // Response from the server
      if(response.data.contains("Error") || response.data.contains("File not found")){
        notifications.show({
          title: 'Error',
          message: 'Please try again',
        })
      }
    } catch (error) {
      console.error(error);
      notifications.show({
        title: 'Error',
        message: "File Not Found",
      })
    }
  }

  return (
    <Menu
      transitionProps={{ transition: 'pop-top-right' }}
      position="top-end"
      width={220}
      withinPortal
    >
      <Menu.Target>
        <Button rightIcon={<IconChevronDown size="1.05rem" stroke={1.5} />} pr={12}>
          Action
        </Button>
      </Menu.Target>
      <Menu.Dropdown>

        <Menu.Item
          icon={<IconSquareCheck size="1rem" color={theme.colors.pink[6]} stroke={1.5} />}
          rightSection={
            <Text size="xs" transform="uppercase" weight={700} color="dimmed">
              {/* Ctrl + T */}
            </Text>
          }
          // onClick={onDownload}
        >
          <a href='`${apiUrl}//api/download'>Download docx</a>
        </Menu.Item>
      </Menu.Dropdown>
    </Menu>
  );
}