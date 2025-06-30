from flask import Flask, request, jsonify

@app.route('/callback-endpoint', methods=['POST'])
def callback_endpoint():
    try:
        # Primanje podataka od Suno API-ja
        callback_data = request.get_json()
        
        # Logiranje za praćenje na Renderu
        print(f"Suno callback received: {callback_data}")
        
        # Provjera statusa
        if callback_data.get('status') == 'SUCCESS':
            task_id = callback_data.get('task_id')
            print(f"Task {task_id} completed successfully!")
            
            # Ovdje možete dodati logiku za čuvanje rezultata
            tracks = callback_data.get('data', [])
            for track in tracks:
                audio_url = track.get('audio_url')
                title = track.get('title')
                print(f"Generated: {title} - {audio_url}")
        
        return jsonify({"status": "received"}), 200
        
    except Exception as e:
        print(f"Callback error: {e}")
        return jsonify({"error": str(e)}), 500
