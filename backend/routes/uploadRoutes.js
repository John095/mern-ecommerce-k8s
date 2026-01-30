import express from 'express';
import { upload, isS3Configured } from '../utils/s3Upload.js';

const router = express.Router();

router.post('/', upload, (req, res) => {
  if (!req.file) {
    return res.status(400).json({ error: 'No file uploaded' });
  }

  // Return appropriate URL based on storage type
  const imageUrl = isS3Configured() 
    ? req.file.location  // S3 URL
    : `/${req.file.path}`; // Local file path

  res.send({
    message: `Image uploaded ${isS3Configured() ? 'to S3' : 'locally'}`,
    imageUrl,
  });
});

export default router;
