import React, { useState } from 'react'
import { Container, LoadingOverlay, Tabs, Grid } from '@mantine/core';
import { DropzoneButton } from "../components/Kfsdoc/Dropzone"
import { ButtonMenu } from "../components/Kfsdoc/Download"
import { Review } from "../components/Kfsdoc/Review"
import { IconArrowsRight, IconArrowsShuffle, IconCheck, IconCopy } from '@tabler/icons-react';

const KfsDocument = () => {
  const [loading, setLoading] = useState(false);
  const [uploadedResult, setUploadedResult] = useState('')

  return (
    <Container my="md">
      <LoadingOverlay visible={loading} overlayBlur={2} />
      <Grid>
        <Grid.Col span={12}>
          <Tabs defaultValue="multi">
            <Tabs.List>
              <Tabs.Tab icon={<IconArrowsRight size="0.8rem" />} value="multi">
                KFS 2 Document
              </Tabs.Tab>
              <Tabs.Tab icon={<IconArrowsShuffle size="0.8rem" />} value="single">
                KFS Single Document
              </Tabs.Tab>
              <Tabs.Tab icon={<IconArrowsShuffle size="0.8rem" />} value="other">
                Other Document Pairing
              </Tabs.Tab>
            </Tabs.List>
            <Tabs.Panel value="multi" pt="xs">
              <Grid>
                <Grid.Col span={6}>
                  <DropzoneButton title="Upload English Document" doctype="english" />
                </Grid.Col>
                <Grid.Col span={6}>
                  <DropzoneButton title="Upload Chinese Document" doctype="chinese" />
                </Grid.Col>
                <Grid.Col span={8}>
                  <Review reviewtype="kfs" setLoading={setLoading} />
                </Grid.Col>
                <Grid.Col span={4}>
                  <ButtonMenu />
                </Grid.Col>
              </Grid>

            </Tabs.Panel>
            <Tabs.Panel value="single" pt="xs">
              <DropzoneButton title="Upload Single Document" doctype="joined" />
            </Tabs.Panel>
            <Tabs.Panel value="other" pt="xs">
              <Grid>
                <Grid.Col span={6}>
                  <DropzoneButton title="Upload English Document" doctype="english" />
                </Grid.Col>
                <Grid.Col span={6}>
                  <DropzoneButton title="Upload Chinese Document" doctype="chinese" />
                </Grid.Col>
                <Grid.Col span={8}>
                  <Review setLoading={setLoading} reviewtype= "oddoc"/>
                </Grid.Col>
                <Grid.Col span={4}>
                  <ButtonMenu />
                </Grid.Col>
              </Grid>
            </Tabs.Panel>
          </Tabs>
        </Grid.Col>


      </Grid>
    </Container>
  )
}

export default KfsDocument