from django.core.management.base import BaseCommand
from dashboard.models import loanType
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = 'Add sample loan products'

    def handle(self, *args, **kwargs):
        user = User.objects.first()
        if not user:
            self.stdout.write(self.style.ERROR('No user found to assign as creator'))
            return

        sample_products = [
            {'name': 'Personal Loan', 'rate': 10.5, 'description': 'Personal loan for various needs', 'need_collateral': False, 'need_guarantor': False, 'market': 'General', 'interest_type': 'Flat Rate'},
            {'name': 'Home Loan', 'rate': 7.2, 'description': 'Loan for home purchase', 'need_collateral': True, 'need_guarantor': False, 'market': 'General', 'interest_type': 'Reducing Balance'},
            {'name': 'Car Loan', 'rate': 8.0, 'description': 'Loan for vehicle purchase', 'need_collateral': True, 'need_guarantor': False, 'market': 'General', 'interest_type': 'Flat Rate'},
            {'name': 'Education Loan', 'rate': 5.5, 'description': 'Loan for education expenses', 'need_collateral': False, 'need_guarantor': True, 'market': 'Students', 'interest_type': 'Flat Rate'},
            {'name': 'Business Loan', 'rate': 12.0, 'description': 'Loan for business capital', 'need_collateral': True, 'need_guarantor': True, 'market': 'Business', 'interest_type': 'Reducing Balance'},
            {'name': 'Agriculture Loan', 'rate': 6.5, 'description': 'Loan for agricultural activities', 'need_collateral': True, 'need_guarantor': False, 'market': 'Farmers', 'interest_type': 'Flat Rate'},
            {'name': 'Travel Loan', 'rate': 9.0, 'description': 'Loan for travel expenses', 'need_collateral': False, 'need_guarantor': False, 'market': 'General', 'interest_type': 'Flat Rate'},
            {'name': 'Medical Loan', 'rate': 7.8, 'description': 'Loan for medical emergencies', 'need_collateral': False, 'need_guarantor': True, 'market': 'General', 'interest_type': 'Flat Rate'},
        ]

        for product_data in sample_products:
            product, created = loanType.objects.get_or_create(
                name=product_data['name'],
                defaults={
                    'rate': product_data['rate'],
                    'description': product_data['description'],
                    'need_collateral': product_data['need_collateral'],
                    'need_guarantor': product_data['need_guarantor'],
                    'market': product_data['market'],
                    'interest_type': product_data['interest_type'],
                    'created_by': user,
                    'company': user.person.company if hasattr(user, 'person') else None,
                    'branch': user.person.branch if hasattr(user, 'person') else None,
                }
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'Created product: {product.name}'))
            else:
                self.stdout.write(f'Product already exists: {product.name}')
