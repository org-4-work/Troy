import { useState } from 'react';
import { Dispatch, SetStateAction } from 'react';
import { useInterval } from '@mantine/hooks';
import { createStyles, Button, Progress } from '@mantine/core';
import axios from 'axios';

const useStyles = createStyles((theme) => ({
  button: {
    position: 'relative',
    transition: 'background-color 150ms ease',
  },

  progress: {
    ...theme.fn.cover(-1),
    height: 'auto',
    backgroundColor: 'transparent',
    zIndex: 0,
  },

  label: {
    position: 'relative',
    zIndex: 1,
  },
}));

type ReviewProps = {
  reviewtype: string;
  setLoading: Dispatch<SetStateAction<boolean>>;
};

export function Review({ reviewtype, setLoading }: ReviewProps) {
  const { classes, theme } = useStyles();
  const [progress, setProgress] = useState(0);
  const [loaded, setLoaded] = useState(false);
  const [link, setLink] = useState("");

  const onDownload = async () => {
    try {
      const response = await axios.get(`http://localhost:5000/api/download/${encodeURIComponent(link)}`, {
        responseType: 'blob',
      });

      const downloadUrl = window.URL.createObjectURL(new Blob([response.data]));
      const downloadLink = document.createElement('a');
      downloadLink.href = downloadUrl;
      downloadLink.setAttribute('download', link.substring(link.lastIndexOf('/') + 1));
      document.body.appendChild(downloadLink);
      downloadLink.click();
      document.body.removeChild(downloadLink);
    } catch (error) {
      console.error(error);
    }
  };


  const onReview = async () => {
    if (reviewtype == "kfs") {
      setLoading(true)

      try {
        const response = await axios.get(`http://localhost:5000/api/review`, {
          headers: {
            'Content-Type': 'multipart/form-data'
          }
        });
        setLoading(false)
        setLoaded(true)
        setLink(response.data.docx_file)
        console.log(response.data); // Response from the server
      } catch (error) {
        setLoading(false)
        console.error(error);
      }
    }
    else {
      try {
        const response = await axios.get(`http://localhost:5000/api/reviewoddoc`, {
          headers: {
            'Content-Type': 'multipart/form-data'
          }
        });
        setLoading(false)
        console.log(response.data); // Response from the server
      } catch (error) {
        setLoading(false)
        console.error(error);
      }
    }

  }
  return (
  <>
      <Button
        fullWidth
        className={classes.button}
        onClick={onReview}
        color={loaded ? 'teal' : theme.primaryColor}
      >
        <div className={classes.label}>
          {progress !== 0 ? 'Reviewing Document' : loaded ? 'Success' : 'Review'}
        </div>
        {progress !== 0 && (
          <Progress
            value={progress}
            className={classes.progress}
            color={theme.fn.rgba(theme.colors[theme.primaryColor][2], 0.35)}
            radius="sm"
          />
        )}
      </Button>
      <br />
      {loaded && (
        <Button
          fullWidth
          className={classes.button}
          color={loaded ? 'teal' : theme.primaryColor}
          onClick={onDownload}
        >
          Download
        </Button>
      )}
      
  </>
  );
}