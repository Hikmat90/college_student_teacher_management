from rest_framework import serializers
from .models import Student, Teacher, AVAILABLE_ID
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

    def validate_username(self, value):
        """Validate that the username does not contain any numeric values."""
        if any(char.isdigit() for char in value):
            raise serializers.ValidationError("Username cannot contain any numeric values.")
        return value

    def validate_roll_no(self, value):
        """Validate that the roll number is numeric."""
        if not value.isdigit():
            raise serializers.ValidationError("Roll no must be numeric.")
        return value

class TeacherSerializer(serializers.ModelSerializer):
    # id_no = serializers.ChoiceField(choices=Teacher.AVAILABLE_ID)  # Ensure id_no validation against available choices
    
    class Meta:
        model = Teacher
        fields = '__all__'

    def validate_username(self, value):
        """Validate that the username does not contain any numeric values."""
        if any(char.isdigit() for char in value):
            raise serializers.ValidationError("Username cannot contain any numeric values.")
        return value
    
    def validate_id_no(self, value):
        # Convert AVAILABLE_ID to a list of its first elements for easy checking
        available_ids = [id_tuple[0] for id_tuple in AVAILABLE_ID]
        if value not in available_ids:
            raise serializers.ValidationError("Invalid ID no.")
        return value