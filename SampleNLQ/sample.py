import json

# Load JSON data
with open('/Volumes/Hmain/script for 50 nlq/nlq_val.json', 'r') as gt_file:
    ground_truth_data = json.load(gt_file)

with open('/Volumes/Hmain/script for 50 nlq/vslnet_9_3220_preds.json', 'r') as preds_file:
    predicted_data = json.load(preds_file)

# Function to calculate Intersection over Union (IoU)
def calculate_iou(gt_start, gt_end, pred_start, pred_end):
    intersection_start = max(gt_start, pred_start)
    intersection_end = min(gt_end, pred_end)
    intersection = max(0, intersection_end - intersection_start)
    union = (gt_end - gt_start) + (pred_end - pred_start) - intersection
    return intersection / union if union != 0 else 0

# Function to extract and sort data based on IoU
def extract_and_sort_data(ground_truth_data, predicted_data):
    results = []
    seen = set()  # To track processed entries and avoid duplicates

    for video in ground_truth_data.get('videos', []):
        for clip in video.get('clips', []):
            for annotation in clip.get('annotations', []):
                for query_index, query in enumerate(annotation.get('language_queries', [])):
                    clip_uid = clip.get('clip_uid')
                    annotation_uid = annotation.get('annotation_uid')
                    
                    for result in predicted_data.get('results', []):
                        if result.get('clip_uid') == clip_uid and result.get('annotation_uid') == annotation_uid:
                            for prediction in result.get('predicted_times', []):
                                if result.get('query_idx') == query_index:
                                    pred_start, pred_end = prediction
                                    key = (clip_uid, annotation_uid, result.get('query_idx'))

                                    if key not in seen:  # Check if this key has been processed
                                        seen.add(key)
                                        clip_start_sec = query.get('clip_start_sec')
                                        clip_end_sec = query.get('clip_end_sec')
                                        iou = calculate_iou(clip_start_sec, clip_end_sec, pred_start, pred_end)
                                        
                                        results.append({
                                            'clip_uid': clip_uid,
                                            'annotation_uid': annotation_uid,
                                            'query_index': query_index,
                                            'query_idx': result.get('query_idx'),
                                            'clip_start_sec': clip_start_sec,
                                            'clip_end_sec': clip_end_sec,
                                            'predicted_start': pred_start,
                                            'predicted_end': pred_end,
                                            'iou': iou,
                                            'query': query.get('query')
                                        })

    # Sort results by IoU in descending order
    results.sort(key=lambda x: x['iou'], reverse=True)
    return results[:50]  # Limit to top 50 results

# Extract and sort data
extracted_data = extract_and_sort_data(ground_truth_data, predicted_data)

# Save the extracted data
with open('/Volumes/Hmain/script for 50 nlq/output7.json', 'w') as file:
    json.dump(extracted_data, file, indent=4)

print("Data saved to 'output6.json'")
