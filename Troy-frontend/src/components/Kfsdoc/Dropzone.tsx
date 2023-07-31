import { useRef, useEffect ,useState} from 'react';
import {LoadingOverlay, Text, Group, Button, createStyles, rem } from '@mantine/core';
import { Dropzone, MIME_TYPES } from '@mantine/dropzone';
import { IconCloudUpload, IconX, IconDownload } from '@tabler/icons-react';
import axios from 'axios';
import FormData from 'form-data'

const useStyles = createStyles((theme) => ({
  wrapper: {
    position: 'relative',
    marginBottom: rem(30),
  },

  dropzone: {
    borderWidth: rem(1),
    paddingBottom: rem(50),
  },

  icon: {
    color: theme.colorScheme === 'dark' ? theme.colors.dark[3] : theme.colors.gray[4],
  },

  control: {
    position: 'absolute',
    width: rem(250),
    left: `calc(50% - ${rem(125)})`,
    bottom: rem(-20),
  },
}));
interface DropzonButtonProps {
  title: string
  doctype: string
}
export function DropzoneButton({ title,doctype }: DropzonButtonProps) {
  // const [visible, { toggle }] = useDisclosure(false);
  const [loading, setloading] = useState(false);
  const [uploadedResult, setUploadedResult] = useState('')
  const { classes, theme } = useStyles();
  const openRef = useRef<() => void>(null);

  const uploadFile = async (file: any) => {
    // Make the API request with the blobData
    const formData = new FormData();
    formData.append(
      'file',
      new Blob([file[0]], { type: 'application/vnd.openxmlformats-officedocument.wordprocessingml.document' }),
      file[0].name
    );
    try {
      const response = await axios.post(``${apiUrl}//api/upload/${doctype}`, formData, {
        headers: {
          'Content-Type': 'multipart/form-data'
        }
      });
      setloading(false)
      setUploadedResult(response.data)
      console.log(response.data); // Response from the server
    } catch (error) {
      console.error(error);
    }
  }
  // file=@KFS - CT European Fund_C.DOCX;type=application/vnd.openxmlformats-officedocument.wordprocessingml.document

  useEffect(() => {
  }, [openRef])

  return (
    <div className={classes.wrapper}>
      
      <Dropzone
        // openRef={openRef}
        onDrop={(files) => {
          setloading(true)
          uploadFile(files)}
        }
        className={classes.dropzone}
        radius="md"
        accept={[MIME_TYPES.docx]}
        maxSize={30 * 1024 ** 2}
      >
        <LoadingOverlay visible={loading} overlayBlur={2} />
        <div style={{ pointerEvents: 'none' }}>
          <Group position="center">
            <Dropzone.Accept>
              <IconDownload
                size={rem(50)}
                color={theme.colors[theme.primaryColor][6]}
                stroke={1.5}
              />
            </Dropzone.Accept>
            <Dropzone.Reject>
              <IconX size={rem(50)} color={theme.colors.red[6]} stroke={1.5} />
            </Dropzone.Reject>
            <Dropzone.Idle>
              <IconCloudUpload
                size={rem(50)}
                color={theme.colorScheme === 'dark' ? theme.colors.dark[0] : theme.black}
                stroke={1.5}
              />
            </Dropzone.Idle>
          </Group>

          <Text ta="center" fw={700} fz="lg" mt="xl">
            <Dropzone.Accept>Drop files here</Dropzone.Accept>
            <Dropzone.Reject>Pdf file less than 30mb</Dropzone.Reject>
            <Dropzone.Idle>{title}</Dropzone.Idle>
          </Text>
          <Text ta="center" fz="sm" mt="xs" c="dimmed">
            Drag&apos;n&apos;drop files here to upload. We can accept only <i>.docx</i> files that
            are less than 30mb in size.
          </Text>
          <Text ta="center" fz="sm" mt="xs" c="dimmed">
            {uploadedResult}
          </Text>
        </div>
      </Dropzone>

      {/* <Button className={classes.control} size="md" radius="xl" onClick={() => openRef.current?.()}>
        Select Document
      </Button> */}
    </div>
  );
}